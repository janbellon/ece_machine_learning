import pandas as pd

# Prétraitement
## 1.
def get_first_n_lines(path: str, lines: int) -> list[str]:
    with open(path, "r") as f:
        head = [next(f) for _ in range(lines)]
    return head

# 2.
def get_dimensions(path: str) -> int:
    first_line = get_first_n_lines(path, 1)[0]
    return len(first_line.split(","))

# 3.
def get_variables_types(path: str) -> list[str]:
    df = pd.read_csv(path)
    print(df.dtypes)

if __name__ == "__main__":
    # 1. 
    """print("== PRETRAITEMENT ==")
    print("== 1 ==")
    print("TR :")
    print("".join(get_first_n_lines("./Training_BOP.csv", 5)))
    print("TS :")
    print("".join(get_first_n_lines("./Testing_BOP.csv", 5)))

    print("== 2 ==")
    print("Dimensions")
    print(f'TR -> {get_dimensions("./Training_BOP.csv")}')
    print(f'TS -> {get_dimensions("./Testing_BOP.csv")}')"""

    get_variables_types("./Training_BOP.csv")


