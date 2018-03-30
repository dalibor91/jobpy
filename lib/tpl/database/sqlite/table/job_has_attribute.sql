CREATE TABLE job_has_attribute(
  `job_id` INTEGER NOT NULL,
  `attribute_id` INTEGER NOT NULL,
  `value` VARCHAR(255) DEFAULT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
);