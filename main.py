#!/usr/bin/env python
# Code by: Mostafa Yasin
# Mail: mostafa.a.yasin@gmail.com
# phone: 01154628593 | 01099169045

char_map = {
    '2': ['a', 'b', 'c', 'A', 'B', 'C'],
    '3': ['d', 'e', 'f', 'D', 'E', 'F'],
    '4': ['g', 'h', 'i', 'G', 'H', 'I'],
    '5': ['j', 'k', 'l' ,'J', 'K', 'L'],
    '6': ['m', 'n', 'o', 'M', 'N','O'],
    '7': ['p', 'q', 'r', 'P', 'Q','R'],
    '8': ['t', 'u', 'v', 'T', 'U','V'],
    '9': ['w', 'x', 'y', 'z', 'W', 'X','Y', 'Z']
}


def validate(number):
    # num must be as 'XXX-XXX-XXXX'
    if len(number) != 12:
        return {'success': False, 'message': "Length must be exactily 12 chars."}

    strs = number.split('-')
    if len(strs) != 3:
        return {'success': False, 'message': "Number must be 3 sections seperated by '-'"}

    try:
        int(strs[0])
    except Exception:
        return {'success': False, 'message': "First section must be int."}

    
    if len(strs[0]) != 3:
        return {'success': False, 'message': "First section length must be 3 digits"}


    if len(strs[1]) != 3:
        return {'success': False, 'message': "Second section length must be 3 digits"}


    if len(strs[2]) != 4:
        return {'success': False, 'message': "Third section length must be 4 digits"}

    if " " in number:
        return {'success': False, 'message': "Spaces are not accepted"}        

    return {'success': True, 'message': "Passed"}


def main():
    cont = "y"
    while cont in ["y", "Y"]:
        valid_input = {'success': False, 'message': ''}

        # while user input is not valid, loop!
        while not valid_input['success']:
            print("=" * 50)
            # Get the user input.
            print("ex: 555-GET-FOOD")
            user_input = raw_input("Enter a 10 char telephone number: ")
            
            # Validate user input
            valid_input = validate(user_input)
            
            # check the validation of user input
            if not valid_input['success']:
                print(valid_input['message'])

        print("You Entered: {}".format(user_input))

        # Loop over user input
        for ch in user_input:
            # Loop over char map
            for num in char_map:
                # If char in use_input exists in current {num: [chars]}
                # replace the char with the num.
                if ch in char_map[num]:
                    user_input = user_input.replace(ch, num)

        # print the result.
        print("-" * 50)
        print("Source number: {}".format(user_input))
        print("-" * 50)

        # Ask the user if he wants to continue
        cont = raw_input("Do you want to continue? (Y/N): ")


if __name__ == "__main__":
    main()