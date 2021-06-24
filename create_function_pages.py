from pathlib import Path


class FunctionPageCreator:
    def __init__(self):
        self.function_list_filename = "power_m_functions.txt"
        self.function_path = Path.cwd().joinpath("functions")

    def run(self):
        self._read_function_list()
        self._structure_function_list()

    def _read_function_list(self):
        with open(self.function_list_filename, "r") as function_list_file:
            self.function_list_raw = function_list_file.read()

        # print(self.function_list_raw)

    def _structure_function_list(self):
        self.function_list = dict()
        header_name = None

        for line in self.function_list_raw.split("\n"):
            if line.strip() == "":
                continue

            elif line.startswith("  "):
                # print(f"\tFunction: {line.strip()}")
                function_name = line.strip().replace(" ", "-").replace(".", "-").lower()

                if "#" in function_name:
                    function_name = function_name.replace("#", "sharp")
                    line = line.replace("#", "\#")

                if "overview" in function_name:
                    continue

                function_page_path = header_path.joinpath(function_name + ".md")

                print(f"Creating function page at: {function_page_path}")

                if not function_page_path.exists():
                    function_page_path.touch()

                with open(function_page_path, "w") as function_page_file:
                    function_page_file.write("---\n")
                    function_page_file.write("---\n\n")
                    function_page_file.write(f"# {line.strip()}\n\n")
                    function_page_file.write(
                        f"Microsoft Docs: [{line.strip()}](https://docs.microsoft.com/en-us/powerquery-m/{function_name})\n\n"
                    )
                    function_page_file.write("## Syntax\n\n")
                    function_page_file.write("```\n")
                    function_page_file.write("Syntax for this function.\n")
                    function_page_file.write("```\n\n")
                    function_page_file.write("## About\n\n")
                    function_page_file.write("About this function.\n\n")

            else:
                # print(f"Header: {line.strip()}")
                header_name = line.strip().replace(" ", "-").lower()

                # print(f"Creating header: {header_name}")

                header_path = self.function_path.joinpath(header_name)

                print(f"Creating header directory at: {header_path}")

                header_path.mkdir(exist_ok=True)

                readme_path = header_path.joinpath("README.md")

                print(f"Creating README at: {readme_path}")

                if not readme_path.exists():
                    readme_path.touch()

                with open(readme_path, "w") as readme_file:
                    readme_file.write("---\n")
                    readme_file.write("---\n\n")
                    readme_file.write(f"# {line.strip()}\n\n")
                    readme_file.write(
                        f"Microsoft Docs: [{line.strip()}](https://docs.microsoft.com/en-us/powerquery-m/{header_name})\n\n"
                    )
                    readme_file.write("About this function group.\n\n")
                    readme_file.write("{% include list.liquid all=true %}")


if __name__ == "__main__":
    process = FunctionPageCreator()
    process.run()
