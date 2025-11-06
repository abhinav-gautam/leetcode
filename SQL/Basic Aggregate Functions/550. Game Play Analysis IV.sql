-- https://leetcode.com/problems/game-play-analysis-iv/?envType=study-plan-v2&envId=top-sql-50
select
    round(
        count(distinct player_id) / (
            select
                count(distinct player_id)
            from
                activity
        ),
        2
    ) as fraction
from
    activity
where
    (player_id, DATE_SUB(event_date, interval 1 day)) in (
        select
            player_id,
            min(event_date) as min_date
        from
            activity
        group by
            player_id
    );