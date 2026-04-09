class StringOperation:
    def __init__(self, text):
        self.text = text

    def update_text(self, new_text):
        self.text = new_text

    def to_upper(self):
        return self.text.upper()
    
    def to_lower(self):
        return self.text.lower()
    
    def reverse(self):
        return self.text[::-1]
    
    def count_vowels(self):
        vowels = "aeiouAEIOU"
        return sum(1 for char in self.text if char in vowels)
    
    def is_palindrome(self):
        return self.text == self.text[::-1]
    
    def display(self):
        return self.text
    

class StringSystem:
    def __init__(self):
        self.obj = None

    def start(self):
        text = input("Enter initial text/sentence: ")
        self.obj = StringOperation(text) 
        self.menu()

    def menu(self):
        while True:
            print("\n--- STRING OPERATION SYSTEM ---")
            print("1. Show String")
            print("2. Convert to Uppercase")
            print("3. Convert to Lowercase")
            print("4. Reverse String")
            print("5. Count Vowels")
            print("6. Check Palindrome")
            print("7. Update String")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Current String:", self.obj.display())
            
            elif choice == "2":
                print("Uppercase:", self.obj.to_upper())
            
            elif choice == "3":
                print("Lowercase:", self.obj.to_lower())
            
            elif choice == "4":
                print("Reversed:", self.obj.reverse())
            
            elif choice == "5":
                print("Vowels:", self.obj.count_vowels())
            
            elif choice == "6":
                if self.obj.is_palindrome():
                    print("It is a Palindrome")
                else:
                    print("Not a Palindrome")
            
            elif choice == "7":
                new_text = input("Enter new string: ")
                self.obj.update_text(new_text)
                print("String Updated Successfully")
            
            elif choice == "0":
                print("Exiting system...")
                break
            
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    app = StringSystem()
    app.start()