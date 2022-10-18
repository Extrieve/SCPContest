#include <iostream>
#include <map>
#include <vector>
 
using namespace std;
 
int main() {
    int n;
	cin >> n;
	map<string, vector<string>> members;
	for(int i = 0; i < n; ++i) {
		string name, designation;
		cin >> name >> designation;
		if(designation == "child")
			designation = "woman";
		members[designation].push_back(name);
	}
	vector<string> designations = {"rat", "woman", "man", "captain"};
	for(const string& designation : designations) {
		for(const string& name : members[designation]) {
			cout << name << '\n';
		}
	}
	
    return 0;
}