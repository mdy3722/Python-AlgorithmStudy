--대장균 개체의 크기를 내름차순으로 정렬했을 때 상위 0% ~ 25% 를 'CRITICAL', 26% ~ 50% 를 'HIGH',
--51% ~ 75% 를 'MEDIUM', 76% ~ 100% 를 'LOW' 라고 분류합니다.
--대장균 개체의 ID(ID) 와 분류된 이름(COLONY_NAME)을 출력하는 SQL 문을 작성해주세요.
--이때 결과는 개체의 ID 에 대해 오름차순 정렬해주세요 .
--단, 총 데이터의 수는 4의 배수이며 같은 사이즈의 대장균 개체가 서로 다른 이름으로 분류되는 경우는 없습니다.

SELECT
  ID,
  CASE NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC)
    WHEN 1 THEN 'CRITICAL'
    WHEN 2 THEN 'HIGH'
    WHEN 3 THEN 'MEDIUM'
    WHEN 4 THEN 'LOW'
  END AS COLONY_NAME
FROM ECOLI_DATA
ORDER BY ID;

-- NTILE 사용 x 버전
WITH ranked AS(
  SELECT ID, SIZE_OF_COLONY, RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) AS r,
          COUNT(*) OVER () AS total
  FROM ECOLI_DATA
)

SELECT ID,
      CASE
        WHEN r <= total * 0.25 THEN 'CRITICAL'
        WHEN r <= total * 0.50 THEN 'HIGH'
        WHEN r <= total * 0.75 THEN 'MEDIUM'
        ELSE 'LOW'
      END AS COLONY_NAME
FROM ranked
ORDER BY ID;