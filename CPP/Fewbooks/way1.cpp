#include <iostream>
#include <stdlib.h>
//input: Arany János;Toldi;10;8

using namespace std;

int main() {
    int n, k = 0;
    cin >> n;
    string s;
    getline(cin, s);
    int y[n];

    for (int i = 0;i < n;i++) {
        string g, h[4], delimiter = ";";
        getline(cin, g);
        size_t pos = 0;

        for(int j = 0; j < 4; j++) {
            pos = g.find(delimiter);
            h[j] = g.substr(0, pos);
            g.erase(0, pos + 1); //1 is delimiter.length()
        }
        int c = atoi(h[2].c_str()),
            d = atoi(h[3].c_str());
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
