SELECT A.`学校`,AVG(`得分`) AS 平均有效分,B.`平均分`,MAX(`得分`) AS 最高有效分,B.`最高分`,MIN(`得分`) AS 最低有效分,B.`最低分`,COUNT(*) AS 有效分数数量,B.`全部分数数量` FROM `scores` A JOIN (
	SELECT scores.`学校`,AVG(`得分`) AS 平均分,MAX(`得分`) AS 最高分,MIN(`得分`) AS 最低分,COUNT(*) AS 全部分数数量 FROM `scores`
	GROUP BY scores.`学校`) B ON A.`学校`=B.`学校`
WHERE `成绩是否有效`='成绩有效'
GROUP BY A.`学校`
ORDER BY 平均有效分 DESC;