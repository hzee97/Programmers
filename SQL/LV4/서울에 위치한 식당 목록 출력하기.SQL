SELECT REST_INFO.REST_ID AS REST_ID, REST_INFO.REST_NAME AS REST_NAME, REST_INFO.FOOD_TYPE AS FOOD_TYPE, REST_INFO.FAVORITES AS FAVORITES, REST_INFO.ADDRESS AS ADDRESS, ROUND(AVG(REST_REVIEW.REVIEW_SCORE),2) AS SCORE
FROM REST_INFO JOIN REST_REVIEW ON REST_INFO.REST_ID = REST_REVIEW.REST_ID
GROUP BY REST_ID
HAVING REST_INFO.ADDRESS LIKE '서울%'
ORDER BY SCORE DESC, FAVORITES DESC