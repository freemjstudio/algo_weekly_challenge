package main

import "fmt"

func main() {
	nums := []int{-1, -1, 0, 1, 1, 0}
	u := pivotIndex(nums)
	fmt.Println(u)
}

func pivotIndex(nums []int) int {
	if len(nums) == 1 {
		return 0
	}
	right_sum := getSum(nums[1:])
	left_sum := 0

	for i := 0; i < len(nums)-1; i++ {
		if left_sum == right_sum {
			return i
		} else {
			left_sum += nums[i]
			right_sum -= nums[i+1]
		}
	}

	if left_sum == right_sum {
		return len(nums) - 1
	}

	return -1
}

func getSum(nums []int) int {
	sum := 0

	for _, val := range nums {
		sum += val
	}
	return sum
}
