#include <iostream>
#include <vector>
#include <map>
 
using namespace std;

int main() {
	int n;
	cin >> n;
	map<string, int> my_map;
	for(int i = 0; i < n; ++i) {
		string name;
		cin >> name;
		if(my_map.count(name) == 1) {
			my_map[name]++;
			cout << name << my_map[name] << '\n';
		}
		else {
			my_map[name] = 0;
			cout << "OK\n";
		}
	}
}