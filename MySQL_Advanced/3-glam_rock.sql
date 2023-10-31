-- 3. Old school band
SELECT band_name, (formed - split) AS lifespan
FROM metal_bands
WHERE main_style = 'Glam rock'
ORDER BY lifespan DESC;
