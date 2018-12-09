#include <iostream>
#include <stdlib.h>
#include <limits>
//input: Arany János;Toldi;10;8

using namespace std;

int main() {
    int n, k = 0;
    cin >> n;
    string s;
    getline(cin, s);
    int y[n];

    for (int i = 0;i < n;i++) {
        int c, d;
        cin.ignore(numeric_limits<int>::max(), ';');
        cin.ignore(numeric_limits<int>::max(), ';');
        cin >> c;
        cin.ignore(1, ';');
        cin >> d;
        if (c-d <= 2) {
            k++;
            y[i] = i + 1;
        }else {
            y[i] = -1;
        }
    }
    cout << k << " ";
    for (int i = 0;i < n;i++) {
        if (y[i] != -1) {
            cout << y[i] << " ";
        }
    }
    return 0;
}
