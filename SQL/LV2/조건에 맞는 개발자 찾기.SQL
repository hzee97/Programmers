SELECT DEVELOPERS.ID AS ID, DEVELOPERS.EMAIL AS EMAIL, DEVELOPERS.FIRST_NAME AS FIRST_NAME, DEVELOPERS.LAST_NAME AS LAST_NAME
FROM DEVELOPERS
WHERE DEVELOPERS.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') OR DEVELOPERS.SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') 
ORDER BY ID ASC