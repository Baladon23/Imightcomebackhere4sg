#include <iostream>
#include <stdlib.h>
#include <sstream>
//input: Arany János;Toldi;10;8

using namespace std;

int main() {
    int n, k = 0;
    cin >> n;
    string s;
    getline(cin, s);
    int y[n];

    for (int i = 0;i < n;i++) {
        string s;
        getline(cin, s, ';');
        getline(cin, s, ';');
        getline(cin, s, ';');
        stringstream ss;
        ss << s;
        int c, d;
        getline(cin, s);
        ss << ' ' << s; //only works with whitespace!
        ss >> c >> d;
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
