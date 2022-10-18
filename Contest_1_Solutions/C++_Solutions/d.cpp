#include <iostream> 
#include <string>
 
using namespace std;
 
int main() {
    string str;
    cin >> str;
    bool first = true;
    while(str.find("WUB") != string::npos) {
        size_t i = str.find("WUB");
        auto it = str.begin() + i;
        str.erase(it, it + 3);
        if(i != 0 && str[i - 1] != ' ') {
            str.insert(i, 1, ' ');
        }
    }
    
    cout << str << endl;
    
    return 0;
}