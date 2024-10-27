

  create or replace view `dataengineerproject-439609`.`dp`.`my_second_dbt_model`
  OPTIONS()
  as -- Use the `ref` function to select from other models

select *
from `dataengineerproject-439609`.`dp`.`my_first_dbt_model`
where id = 1;

