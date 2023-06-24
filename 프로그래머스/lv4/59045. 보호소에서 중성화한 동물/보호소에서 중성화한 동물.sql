-- 코드를 입력하세요
-- 보호소 들어올 때 중성화 x
-- 보호소 나갈 때 중성화 o

select i.animal_id as ANIMAL_ID, i.animal_type ANIMAL_TYPE, i.name NAME
from ANIMAL_INS i
left join ANIMAL_OUTS o 
on i.animal_id = o.animal_id
where i.sex_upon_intake like 'In%' and (o.sex_upon_outcome like 'S%' or o.sex_upon_outcome like 'N%');