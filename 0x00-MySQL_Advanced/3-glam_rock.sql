-- Create a temporary table to calculate lifespan
CREATE TEMPORARY TABLE BandLifespan AS
SELECT
    band_name,
    CASE
        WHEN formed = 'N/A' OR formed = '' OR split = 'N/A' OR split = '' THEN NULL
        ELSE YEAR('2022-01-01') - YEAR(CONCAT(formed, '-01-01'))
    END AS lifespan
FROM metal_bands;

-- List Glam rock bands ranked by longevity
SELECT band_name, lifespan
FROM BandLifespan
WHERE band_name IN (
    SELECT band_name
    FROM metal_bands
    WHERE style LIKE '%Glam rock%'
)
ORDER BY lifespan;

