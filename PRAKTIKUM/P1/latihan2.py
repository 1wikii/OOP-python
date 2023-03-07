'''#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Masukkan jumlah baris: ";
    cin >> n;

    for (int i = 1; i <= n; i++) { // perulangan untuk baris
        for (int j = 1; j <= i; j++) { // perulangan untuk kolom
            cout << "* ";
        }
        cout << endl; // pindah ke baris berikutnya
    }
    return 0;
}'''

n = int(input('Masukkan jumlah baris : '))

for i in range(n):
    for j in range(i+1):
        print('* ',end="")
    print("")