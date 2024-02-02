public class NumberOfIslands {
    public static void main(String[] args) {
        char[][] grid = {
                {'1','0','1','1','0','1','1'}
        };
        int result = new Solution().numIslands(grid);
        System.out.println(result);
    }

    static class Solution {
        public int numIslands(char[][] grid) {
            Set<Point> discovered = new HashSet<>();

            // 인접 land 검사
            int count = 0;
            for (int y = 0; y < grid[0].length; y++) {
                for (int x = 0; x < grid.length; x++) {
                    if (grid[x][y] == '1' && !discovered.contains(new Point(x,y))) {
                        check(grid, x, y, discovered);
                        count++;
                    }
                }
            }
            return count;
        }

        private void check(char[][] grid, int x, int y, Set<Point> discovered) {
            Point point = new Point(x, y);

            if (discovered.contains(point)) {
                return;
            }

            if (x >= grid.length || y >= grid[0].length) {
                return;
            }

            if (grid[x][y] == '0') {
                return;
            }

            discovered.add(point);

            // top
            if (x + 1 < grid.length && grid[x+1][y] != 0) {
                check(grid, x+1, y, discovered);
            }

            // bottom
            if (x - 1 >= 0 && grid[x-1][y] != 0) {
                check(grid, x-1, y, discovered);
            }

            // left
            if (y - 1 >= 0 && grid[x][y-1] != 0) {
                check(grid, x, y-1, discovered);
            }

            // right
            if (y + 1 < grid[0].length && grid[x][y+1] != 0) {
                check(grid, x, y+1, discovered);
            }
        }

        static class Point {
            int x;
            int y;
            Point(int x, int y) {
                this.x = x;
                this.y = y;
            }

            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (!(o instanceof Point point)) return false;

                if (x != point.x) return false;
                return y == point.y;
            }

            @Override
            public int hashCode() {
                int result = x;
                result = 31 * result + y;
                return result;
            }
        }
    }
}
