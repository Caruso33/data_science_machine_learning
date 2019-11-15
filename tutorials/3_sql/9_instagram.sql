-- FIRST
-- source 9_instagram_data.sql;
--
-- find 5 oldest users
SELECT
  *
FROM users
ORDER BY
  created_at ASC
LIMIT
  5;
--
  -- what day of week do most users register on?
SELECT
  DAYNAME(created_at) AS DayName,
  COUNT(1) as Total
FROM users
GROUP BY
  DayName
ORDER BY
  Total DESC;
--
  -- users who never posted photo
SELECT
  username
FROM users
LEFT JOIN photos ON users.id = photos.user_id
WHERE
  image_url IS NULL;
--
SELECT
  SUM(1)
FROM users
LEFT JOIN photos ON users.id = photos.user_id
WHERE
  image_url IS NULL
GROUP BY
  image_url IS NULL;
--
  -- who has most likes on single photo
  WITH MaxPhotoId AS (
    SELECT
      photo_id AS Photo
    FROM likes
    GROUP BY
      Photo
    ORDER BY
      COUNT(Photo) DESC
    LIMIT
      1
  )
SELECT
  username,
  image_url
FROM MaxPhotoId
INNER JOIN photos
INNER JOIN users
WHERE
  photos.id = Photo
  AND users.id = user_id;
--
  -- how may times does average user post?
SELECT
  (
    SELECT
      COUNT(photos.id)
    FROM photos
  ) / (
    SELECT
      COUNT(users.id)
    FROM users
  ) AS AvgPostsPerUser;
--
  -- top 5 most commonly used hashtags?
SELECT
  tags.tag_name,
  COUNT(*) AS total
FROM photo_tags
INNER JOIN tags ON photo_tags.photo_id = tags.id
GROUP BY
  tags.id
ORDER BY
  total DESC
LIMIT
  5;
--
  -- users whi have liked every single photo
SELECT
  username,
  user_id,
  COUNT(*) AS total
FROM users
INNER JOIN likes ON users.id = likes.user_id
GROUP BY
  likes.user_id
-- HAVING is needed as WHERE comes before GROUP BY clause
-- and hence wouldn't work
HAVING
  total = (
    SELECT
      COUNT(*)
    FROM photos
  );