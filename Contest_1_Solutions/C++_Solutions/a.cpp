#include <iostream>
#include <vector>
#include <set>
 
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int i = 0; i < t; ++i) {
		int n;
		cin >> n;
		vector<int> vec(n);
		for(int& i : vec)
			cin >> i;
		set<int> s(vec.begin(), vec.end());
		if(vec.size() == s.size()) {
			cout << "YES\n";
		}
		else {
			cout << "NO\n";
		}
	}
}