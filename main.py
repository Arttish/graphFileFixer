import os


def list_files_in_directory(directory_path):
    if not os.path.exists(directory_path):
        print(f"Путь {directory_path} не существует.")
        return

    all_files_and_folders = os.listdir(directory_path)
    files_only = [f for f in all_files_and_folders if os.path.isfile(os.path.join(directory_path, f))]
    return files_only


if __name__ == "__main__":
    for filename in list_files_in_directory("input"):
        with open(f"input/{filename}", "r") as original:
            with open(f"output/{filename}", "w") as processed:
                line = original.readline()
                processed.write(line)
                vertices_count = int(line.strip().split()[1])
                processed.write(original.readline())
                for _ in range(vertices_count):
                    line = original.readline()
                    vertex = line.strip().split()
                    vertex[-1] = str(int(float(vertex[-1])))
                    vertex[-2] = str(int(float(vertex[-2])))
                    vertex.append('\n')
                    vertex = ' '.join(vertex)
                    processed.write(vertex)
                for line in original:
                    processed.write(line)

