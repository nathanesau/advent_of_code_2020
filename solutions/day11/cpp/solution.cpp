#include <map>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string_view>
#include <cstring>
#include <fstream>

int seat_count_adj(const std::vector<std::vector<char>> &grid, int i, int j) {
    int count = 0;
    if (i-1 >= 0 && grid[i-1][j] == '#') // up
        count += 1;
    if (i+1 < grid.size() && grid[i+1][j] == '#') // down
        count += 1;
    if (j-1 >= 0 && grid[i][j-1] == '#') // left
        count += 1;
    if (j+1 < grid[0].size() && grid[i][j+1] == '#') // right
        count += 1;
    if (i-1 >= 0 && j-1 >= 0 && grid[i-1][j-1] == '#') // up -left
        count += 1;
    if (i+1 < grid.size() && j+1 < grid[0].size() && grid[i+1][j+1] == '#') // down-right
        count += 1;
    if (i+1 < grid.size() && j-1 >= 0 && grid[i+1][j-1] == '#') // down-left
        count += 1;
    if (i-1 >= 0 && j+1 < grid[0].size() && grid[i-1][j+1] == '#') // up-right
        count += 1;
    return count;
}

bool shuffle_seats_adj(std::vector<std::vector<char>> &grid) {
    std::map<std::pair<int, int>, char> adj;
    for (int i = 0; i < grid.size(); i++) {
        for(int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '.')
                continue;
            if (grid[i][j] == 'L' && seat_count_adj(grid, i, j) == 0)
                adj[std::make_pair(i, j)] = '#';
            if (grid[i][j] == '#' && seat_count_adj(grid, i, j) >= 4)
                adj[std::make_pair(i, j)] = 'L';
        }
    }
    for (auto &it : adj) {
        grid[it.first.first][it.first.second] = it.second;
    }
    return !adj.empty(); 
}

int solution_1(std::vector<std::vector<char>> &grid) {
    while (shuffle_seats_adj(grid)) {
        continue;
    }
    int total = 0;
    for (int i = 0; i < grid.size(); i++) {
        total += std::count(grid[i].begin(), grid[i].end(), '#');
    }
    return total;
}

char get_first_seat_left(const std::vector<std::vector<char>> &grid, int i, int j) {
    int col = j - 1;
    while(col >= 0) {
        if (grid[i][col] != '.')
            return grid[i][col];
        col -= 1;
    }
    return '\0';
}

char get_first_seat_right(const std::vector<std::vector<char>> &grid, int i, int j) {
    int col = j + 1;
    while(col <= grid[0].size() - 1) {
        if (grid[i][col] != '.')
            return grid[i][col];
        col += 1;
    }
    return '\0';
}

char get_first_seat_up(const std::vector<std::vector<char>> &grid, int i, int j) {
    int row = i - 1;
    while (row >= 0) {
        if (grid[row][j] != '.')
            return grid[row][j];
        row -= 1;
    }
    return '\0';
}

char get_first_seat_down(const std::vector<std::vector<char>> &grid, int i, int j) {
    int row = i + 1;
    while (row <= grid.size() - 1) {
        if (grid[row][j] != '.') {
            return grid[row][j];
        }
        row += 1;
    }
    return '\0';
}

char get_first_seat_up_left(const std::vector<std::vector<char>> &grid, int i, int j) {
    int row = i - 1;
    int col = j - 1;
    while (row >= 0 && col >= 0) {
        if (grid[row][col] != '.')
            return grid[row][col];
        row -= 1;
        col -= 1;
    }
    return '\0';
}

char get_first_seat_down_right(const std::vector<std::vector<char>> &grid, int i, int j) {
    int row = i + 1;
    int col = j + 1;
    while (row <= grid.size() - 1 && col <= grid[0].size() - 1) {
        if (grid[row][col] != '.')
            return grid[row][col];
        row += 1;
        col += 1;
    }
    return '\0';
}

char get_first_seat_up_right(const std::vector<std::vector<char>> &grid, int i, int j) {
    int row = i - 1;
    int col = j + 1;
    while (row >= 0 && col <= grid[0].size() - 1) {
        if (grid[row][col] != '.')
            return grid[row][col];
        row -= 1;
        col += 1;
    }
    return '\0';
}

char get_first_seat_down_left(const std::vector<std::vector<char>> &grid, int i, int j) {
    int row = i + 1;
    int col = j - 1;
    while (row <= grid.size() - 1 && col >= 0) {
        if (grid[row][col] != '.')
            return grid[row][col];
        row += 1;
        col -= 1;
    }
    return '\0';
}

int seat_count_vis(const std::vector<std::vector<char>> &grid, int i, int j) {
    int count = 0;
    if (get_first_seat_up(grid, i, j) == '#') // up
        count += 1;
    if (get_first_seat_down(grid, i, j) == '#') // down
        count += 1;
    if (get_first_seat_left(grid, i, j) == '#') // left
        count += 1;
    if (get_first_seat_right(grid, i, j) == '#') // right
        count += 1;
    if (get_first_seat_up_left(grid, i, j) == '#') // up-left
        count += 1;
    if (get_first_seat_down_right(grid, i, j) == '#') // down-right
        count += 1;
    if (get_first_seat_down_left(grid, i, j) == '#') // down-left
        count += 1;
    if (get_first_seat_up_right(grid, i, j) == '#') // up-right
        count += 1;
    return count;
}

bool shuffle_seats_vis(std::vector<std::vector<char>> &grid) {
    std::map<std::pair<int, int>, char> adj;
    for (int i = 0; i < grid.size(); i++) {
        for(int j = 0; j < grid[0].size(); j++) {
            if (grid[i][j] == '.')
                continue;
            if (grid[i][j] == 'L' && seat_count_vis(grid, i, j) == 0)
                adj[std::make_pair(i, j)] = '#';
            if (grid[i][j] == '#' && seat_count_vis(grid, i, j) >= 5)
                adj[std::make_pair(i, j)] = 'L';
        }
    }
    for (auto &it : adj) {
        grid[it.first.first][it.first.second] = it.second;
    }
    return !adj.empty(); 
}

int solution_2(std::vector<std::vector<char>> &grid) {
    while (shuffle_seats_vis(grid)) {
        continue;
    }
    int total = 0;
    for (int i = 0; i < grid.size(); i++) {
        total += std::count(grid[i].begin(), grid[i].end(), '#');
    }
    return total;
}

void test_solution_1_example() {
    std::vector<std::string> lines = {
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL"
    };
    std::vector<std::vector<char>> grid;
    for(auto &line : lines) {
        grid.push_back(std::vector<char>(line.begin(), line.end()));
    }
    int s1 = solution_1(grid);
    std::cout << "test_solution_1_example: " << s1 << std::endl;
}

void test_solution_1() {
    std::vector<std::vector<char>> grid;
    std::ifstream in("assets/input.txt");
    if (in.is_open()) {
        std::string line;
        while(getline(in, line)) {
            grid.push_back(std::vector<char>(line.begin(), line.end()));
        }
    }
    int s1 = solution_1(grid);
    std::cout << "test_solution_1: " << s1 << std::endl;
}

void test_solution_2_example() {
    std::vector<std::string> lines = {
        "L.LL.LL.LL",
        "LLLLLLL.LL",
        "L.L.L..L..",
        "LLLL.LL.LL",
        "L.LL.LL.LL",
        "L.LLLLL.LL",
        "..L.L.....",
        "LLLLLLLLLL",
        "L.LLLLLL.L",
        "L.LLLLL.LL"
    };
    std::vector<std::vector<char>> grid;
    for(auto &line : lines) {
        grid.push_back(std::vector<char>(line.begin(), line.end()));
    }
    int s2 = solution_2(grid);
    std::cout << "test_solution_2_example: " << s2 << std::endl;
}

void test_solution_2() {
    std::vector<std::vector<char>> grid;
    std::ifstream in("assets/input.txt");
    if (in.is_open()) {
        std::string line;
        while(getline(in, line)) {
            grid.push_back(std::vector<char>(line.begin(), line.end()));
        }
    }
    int s2 = solution_2(grid);
    std::cout << "test_solution_2: " << s2 << std::endl;
}

/**
 * Timing results (g++ -O2 solution.cpp -o solution)
 * 
 * [esna0001@manjaro-linux build]$ time ./solution
 * test_solution_1_example: 37
 * test_solution_1: 2361
 * 
 * real    0m0.104s
 * user    0m0.103s
 * sys     0m0.000s
 * 
 * Python (not compiled) takes 3 seconds
 * 
 * So c++ is about 30 times faster here with similar implementation.
 */

int main() {
    test_solution_1_example();
    test_solution_1();
    test_solution_2_example();
    test_solution_2();
    return 0;
}
