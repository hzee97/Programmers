SELECT COUNT(FISH_INFO.ID) AS FISH_COUNT, FISH_NAME_INFO.FISH_NAME AS FISH_NAME
FROM FISH_INFO JOIN FISH_NAME_INFO ON FISH_INFO.FISH_TYPE = FISH_NAME_INFO.FISH_TYPE
GROUP BY FISH_NAME
ORDER BY FISH_COUNT DESC