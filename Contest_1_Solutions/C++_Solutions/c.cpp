#include <iostream>
 
using namespace std;
 
int main() {
    int min_capacity = 0, n;
    cin >> n;
    int exit, enter, total = 0;
    for(int i = 0; i < n; ++i) {
        cin >> exit >> enter;
        total = total - exit + enter;
        min_capacity = max(total, min_capacity);
    }
    cout << min_capacity << '\n';
    return 0;
}