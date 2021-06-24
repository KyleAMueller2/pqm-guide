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
        current_header = None
        sort_level = 1

        for line in self.function_list_raw.split("\n"):
            if line.strip() == "":
                pass

            elif line.startswith("  "):
                # print(f"\tFunction: {line.strip()}")
                pass

            else:
                # print(f"Header: {line.strip()}")
                header_name = line.strip().replace(" ", "-").lower()

                if current_header:
                    sort_level += 1

                current_header = f"{sort_level:02d}_{header_name}"

                # print(f"Creating header: {current_header}")

                header_path = self.function_path.joinpath(current_header)

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


if __name__ == "__main__":
    process = FunctionPageCreator()
    process.run()
