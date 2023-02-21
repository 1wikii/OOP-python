'''// #include <iostream>
// using namespace std;

// bool isPalindrome(string word) { //katak
//     int i = 0;
//     int j = word.length() - 1;

//     while (i < j) {
//         // Mencocokkan antar huruf
//         if (word[i] != word[j]) {
//             return false;
//         }
//         // Penunjuk akan bergeser
//         i++;
//         j--;
//     }

//     return true;
// }

// int main() {
//     string kata;
//     cout << "Masukkan kata: ";
//     cin >> kata;
    
//     if (isPalindrome(kata)) {
//         cout << "Kata " << kata << " merupakan Palindrome!!\n";
//     } else {
//         cout << "Kata " << kata << " bukan merupakan Palindrome!!\n";
//     }
//     return 0;
// } '''

def palidrome(word:str):
    j = len(word)-1

    for x in range(j+1):
        if word[x] != word[j-x]:
            return False    
    return True

kata = input("Kata ? ")

if palidrome(kata):
    print("Benar")
else:
    print("Salah")
