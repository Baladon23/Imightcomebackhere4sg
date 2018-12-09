#include <iostream>
#include <stdlib.h>
//input example in the first code
 
using namespace std;
 
int main() {
    int n, k = 0;
    cin >> n;
    string s;
    getline(cin, s);
    int y[n];
 
    for (int i = 0;i < n;i++) {
        char C;
        do {cin >> C;} while (C != ';');
        do {cin >> C;} while (C != ';');
        int c, d;
        cin >> c >> C >> d;
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
