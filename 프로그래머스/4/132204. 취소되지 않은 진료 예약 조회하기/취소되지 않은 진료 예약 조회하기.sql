SELECT APNT_NO, PT_NAME, A.PT_NO, A.MCDP_CD, DR_NAME, APNT_YMD
FROM APPOINTMENT A
LEFT JOIN PATIENT P ON A.PT_NO = P.PT_NO
LEFT JOIN DOCTOR D ON A.MDDR_ID = D.DR_ID
WHERE
    APNT_YMD LIKE '2022-04-13%' AND
    APNT_CNCL_YN = 'N' AND
    A.MCDP_CD = 'CS'
ORDER BY APNT_YMD