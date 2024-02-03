package org.ep.java.backjoon;

import java.util.Scanner;
import java.util.StringJoiner;

/**
 * @see <a href="https://www.acmicpc.net/problem/11729">하노이 탑 이동 순서</a>
 */
public class Problem11729 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int size = sc.nextInt();
        StringJoiner stringJoiner = new StringJoiner("\n");
        recursion(size, 1, 3, 2, stringJoiner);
        System.out.println((stringJoiner.length() + 1) / 4);
        System.out.println(stringJoiner);
    }

    private static void recursion(int size, int start, int dest, int temp, StringJoiner stringJoiner) {
        if (size == 1) {
            stringJoiner.add(start + " " + dest);
        } else {
            recursion(size - 1, start, temp, dest, stringJoiner);
            stringJoiner.add(start + " " + dest);
            recursion(size - 1, temp, dest, start, stringJoiner);
        }
    }
}
