CREATE TABLE job_log(
  `id` INTEGER PRIMARY KEY AUTOINCREMENT,
  `uid` VARCHAR(46) NOT NULL,
  `status` VARCHAR(255) DEFAULT NULL,
  `value` VARCHAR(255) DEFAULT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP
);