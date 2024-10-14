import importlib
data_helper = importlib.import_module("data-helper")

#import data_helper

def main():
    

    random_date = data_helper.random_date()
    random_string = data_helper.random_string(10)
    random_integer = data_helper.random_integer()
    random_double = data_helper.random_double()
    
    print(f"Random Date: {random_date.strftime('%Y-%m-%d')}")
    print(f"Random String: {random_string}")
    print(f"Random Integer: {random_integer}")
    print(f"Random Double: {random_double:.2f}")

if __name__ == "__main__":
    main()