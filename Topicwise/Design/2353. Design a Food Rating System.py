# https://leetcode.com/problems/design-a-food-rating-system/description/?envType=daily-question&envId=2025-09-17

from typing import List
import heapq


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings
        self.cuisineRatingsHeap = {}
        self.foodIndex = {}

        for index, cuisine in enumerate(cuisines):
            self.foodIndex[self.foods[index]] = (index, ratings[index])
            heapq.heappush(
                self.cuisineRatingsHeap.setdefault(cuisine, []),
                (-self.ratings[index], self.foods[index]),
            )

    def changeRating(self, food: str, newRating: int) -> None:
        index, _ = self.foodIndex[food]
        self.ratings[index] = newRating
        self.foodIndex[food] = (index, newRating)

        # Update cuisine ratings heap
        heap = self.cuisineRatingsHeap[self.cuisines[index]]
        heapq.heappush(heap, (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisineRatingsHeap[cuisine]
        while heap:
            rating, food = heap[0]
            if self.foodIndex[food][1] == -rating:
                return food
            heapq.heappop(heap)
        return

    def __str__(self):
        return (
            f"{self.foods}, {self.cuisines}, {self.ratings}, {self.cuisineRatingsHeap}"
        )


foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

obj = FoodRatings(foods, cuisines, ratings)
obj.changeRating("sushi", 14)
obj.changeRating("miso", 14)
print(obj)
print(obj.highestRated("japanese"))
print(obj)
