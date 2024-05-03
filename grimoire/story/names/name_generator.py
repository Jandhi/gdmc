from dataclasses import dataclass

from ..core.assets.asset import Asset
from ..core.generator.module import Module


class NamingSchema(Asset):
    rules: dict[str, str | list[str] | dict[str, int]]


class NameGenerator(Module):
    @dataclass
    class Context:
        schema: NamingSchema
        args: dict[str, any]

    @property
    def context(self):
        return self.__context_stack[-1]

    @property
    def args(self):
        return self.context.args

    @property
    def schema(self):
        return self.context.schema

    def push_ctx(self, ctx: Context):
        self.__context_stack.append(ctx)

    def pop_ctx(self) -> Context:
        return self.__context_stack.pop(-1)

    def __init__(self):
        self.init_rng_from_world_seed()
        # We use a stack for the contexts so the name generator can call multiple schemas recursively
        self.__context_stack: list[NameGenerator.Context] = []

    @Module.main
    def generate_name(
        self, rule_name: str, schema: NamingSchema, args: dict[str, any] = None
    ) -> tuple[str, dict]:
        self.push_ctx(NameGenerator.Context(schema, args or {}))
        return self.__invoke_rule(rule_name), self.args

    # Returns the output of a rule
    def __invoke_rule(self, rule_name: str):
        rule = self.schema.rules[rule_name]

        if isinstance(rule, list):
            return self.__parse_rule(self.rng.choose(rule))
        if isinstance(rule, dict):
            parsed_rules = {
                name: (odds if isinstance(odds, int) else int(self.__parse_rule(odds)))
                for name, odds in rule.items()
            }
            return self.__parse_rule(self.rng.choose_weighted(parsed_rules))

        return self.__parse_rule(rule)

    # Parses the text of a rule
    def __parse_rule(self, rule: str):
        result = ""

        while "<" in rule:
            start_index = rule.index("<")
            result += rule[:start_index]
            rule = rule[start_index:]

            if ">" not in rule:
                self.raise_error(
                    f'Malformed rule "{rule}" in schema {self.schema.name}'
                )

            end_index = rule.index(">")
            command = rule[: end_index + 1].removeprefix("<").removesuffix(">")
            rule = rule[end_index + 1 :]
            result += self.__parse_cmd(command)
        result += rule
        return result

    # Parses individual command in <> sequence
    def __parse_cmd(self, tag: str) -> str:
        args = map(str.strip, tag.split(","))
        result = ""

        for arg in args:
            # This argument represents a chance of the rule applying.
            # Should be first so as to avoid side effects with adding tags, etc
            if arg.startswith("%"):
                chance = float(arg[1:])
                int_chance = int(100 * chance)
                if self.rng.chance(int_chance, 10000):
                    continue
                else:
                    return ""

            result += self.__parse_arg(arg)

        return result

    def __parse_arg(self, arg: str) -> str:
        if arg.startswith("+"):
            tag = arg[1:]
            self.__add_tag(tag)
            return ""
        if arg.startswith("-"):
            tag = arg[1:]
            self.__remove_tag(tag)
            return ""
        if arg.startswith("$"):
            arg_name = arg[1:]
            value = self.__get_arg(arg_name)
            if value is None:
                self.raise_error(f"Arg {arg_name} does not exist!")
            return value
        if arg.startswith("?"):
            return self.__interpret_tag(arg)
        if arg.startswith("#"):
            return self.__interpret_arg(arg)
        # LITERAL
        return arg[1:-1] if arg.startswith("'") else self.__invoke_rule(arg)

    # TODO: Improve name and description
    def __interpret_arg(self, arg):
        """
        Parses the argument to extract schema and rule names, finds the naming schema,
        invokes the specified rule, and returns the result.

        Args:
            arg (str): The argument containing the schema and rule names.

        Returns:
            The result of invoking the specified rule.

        Raises:
            This function does not raise any exceptions.
        """

        parts = arg[1:].split(":")
        schema_name = parts[0]
        rule_name = parts[1]

        schema = NamingSchema.find(schema_name)
        if schema is None:
            self.raise_error(f"Schema {schema_name} does not exist!")
        self.push_ctx(NameGenerator.Context(schema, self.args))
        result = self.__invoke_rule(rule_name)
        self.pop_ctx()

        return result

    # TODO: Improve name and description
    def __interpret_tag(self, arg):
        """
        Parses the argument to extract tag, on_true, and on_false values, checks the tag condition,
        and recursively parses the corresponding value based on the tag condition.

        Args:
            arg (str): The argument containing the tag, on_true, and on_false values.

        Returns:
            The result of parsing the value based on the tag condition.

        Raises:
            This function does not raise any exceptions.
        """

        parts = arg[1:].split(":")
        tag = parts[0]
        args = parts[1].split("|")
        on_true = args[0]
        on_false = args[1]
        return self.__parse_arg(on_true if self.__has_tag(tag) else on_false)

    def __add_tag(self, tag: str) -> None:
        if "tags" not in self.args:
            self.args["tags"] = []

        if tag not in self.args["tags"]:
            self.args["tags"].append(tag)

    def __remove_tag(self, tag: str) -> None:
        if "tags" not in self.args:
            return

        if tag not in self.args["tags"]:
            return

        tags: list[str] = self.args["tags"]
        tags.remove(tag)

    def __has_tag(self, tag: str) -> bool:
        return False if "tags" not in self.args else tag in self.args["tags"]

    def __get_arg(self, arg_name: str) -> any:
        return self.args[arg_name] if arg_name in self.args else None
