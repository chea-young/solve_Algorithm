#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;

/*

Equilateral :  세 변의 길이가 모두 같은 경우
Isosceles : 두 변의 길이만 같은 경우
Scalene : 세 변의 길이가 모두 다른 경우

*/

int main() {
    const string EQUILATERAL = "Equilateral";
    const string ISOSCELES = "Isosceles";
    const string SCALENE = "Scalene";
    const string INVALID = "Invalid";

    while(1) {
        vector<int> sides(3);
        for (int i = 0; i < 3; i ++) {
            std::cin >> sides[i];
        }

        sort(sides.begin(), sides.end());

        if (sides[2] != 0 && sides[2] >= sides[0] + sides[1]) {
            std::cout << INVALID << "\n";
            continue;
        }

        if (sides[0] == sides[1]  && sides[1] == sides[2]) {
            if (sides[0] == 0) {
                break;
            } else {
                std::cout << EQUILATERAL;
            }
        } else if ((sides[0] == sides[1] && sides[1] != sides[2]) ||
                   (sides[1] == sides[2] && sides[1] != sides[0]) ||
                   (sides[0] == sides[2] && sides[1] != sides[2]) ) {
            std::cout << ISOSCELES;
        } else if (sides[0] != sides[1] && sides[1] != sides[2] && sides[0] != sides[2]) {
            std::cout << SCALENE;
        }

        std::cout << "\n";
    }
}