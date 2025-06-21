"""
1.Turn the following snippet into a function:

numbers = [1,2,3,4,5]
squares = []
for n in numbers:
squares.append(n*n)
print(squares)
Requirements:
Create def compute_squares(nums: list[int]) -> list[int]
Add a docstring and type hints
Call it on at least two different lists

"""



def compute_squares(nums: list[int]) -> list[int]:
    square_list = []
    for i in nums:
        square_list.append(i*i)
    return square_list






"""
2.Write a function that reads a text file and returns its
lines.
Use with open(...) as f:
Catch and handle FileNotFoundError with a user-friendly message.
From main(), prompt user for file name, call read_lines, then print line
count

"""







def file_access(filename):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print("file not found.")
        return []


def main():
    filename = input("Enter your file name : ")
    lines = file_access(filename)
    print(f"Number of lines present in file =  {len(lines)}")









if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    sq_list = compute_squares(nums)
    print(sq_list)
    main()
