import os, json, math, re
from datetime import datetime, time


def calculate_points_fom_totals(
    receiptTotal,
):  # 50 points if the total is a round dollar amount with no cents.
    if receiptTotal % 1 == 0:
        return 50
    else:
        return 0


def calculate_points_from_retail_name(
    str,
):  # Function returns the number of points based on number of alphanumeric characters in the retailer Name
    retailPoints = len(re.findall("\w", str))  # return
    return retailPoints


def calculate_points_based_on_total(
    receiptTotal,
):  # Function returns 25 points if the total in the receipt is a multiple of 0.25 else returns 0
    if receiptTotal % 0.25 != 0:
        receiptPoints = 0
    elif receiptTotal % 0.25 == 0:
        receiptPoints = 25
    return receiptPoints


def calculate_points_based_on_number_of_items(
    itemslist,
):  # Function returns 5 points for every two items on the receipt else returns 0
    if len(itemslist) > 1:
        pointsForTwoItems = int(len(itemslist) / 2)
        totalItemPoints = pointsForTwoItems * 5
        return totalItemPoints
    else:
        return 0


def calculate_points_based_description(
    itemsList,
):  # Function returns the points calculation based on the length of the description of all items in the receipt
    descriptionPoints = 0
    for x in itemsList:
        descriptionString = x["shortDescription"].strip()
        if len(descriptionString) % 3 == 0:
            descriptionPoints = descriptionPoints + math.ceil((0.2 * float(x["price"])))
    return descriptionPoints


def calculate_points_based_on_day_type(
    purchaseDate,
):  # Function returns value 6 if the day in the receipt is odd else returns 0
    oddDayPoints = 0
    purchaseDateObject = datetime.strptime(purchaseDate, "%Y-%m-%d")
    purchaseDay = purchaseDateObject.day
    if purchaseDay % 2 != 0:
        oddDayPoints = 6
    return oddDayPoints


def calculate_points_based_on_time(
    timeValue,
):  # Function returns 10 points if the purchase time occured between 2pm - 4pm
    timePoints = 0
    timeObject = datetime.strptime(timeValue, "%H:%M").time()
    starttime = time(14, 0)
    stoptime = time(16, 0)
    if timeObject > starttime and timeObject < stoptime:
        timePoints = 10
    return timePoints


def calculateTotalPoints(
    json,
):  # Function calculates the total points by summing up points from various functions
    totalPoints = calculate_points_from_retail_name(str(json["retailer"]))
    totalPoints += calculate_points_fom_totals(float(json["total"]))
    totalPoints += calculate_points_based_on_total(float(json["total"]))
    totalPoints += calculate_points_based_on_number_of_items(json["items"])
    totalPoints += calculate_points_based_description(json["items"])
    totalPoints += calculate_points_based_on_day_type(json["purchaseDate"])
    totalPoints += calculate_points_based_on_time(json["purchaseTime"])
    return totalPoints
