# Environment variable (this would be set somewhere in your environment or passed as input)
env = "staging"  # Can be 'development', 'staging', or 'production'

# === if-else Example ===
if env == "development":
    db_url = "dev-db.example.com"
    debug_mode = True
    log_level = "DEBUG"
elif env == "staging":
    db_url = "staging-db.example.com"
    debug_mode = False
    log_level = "INFO"
elif env == "production":
    db_url = "prod-db.example.com"
    debug_mode = False
    log_level = "ERROR"
else:
    db_url = None
    debug_mode = False
    log_level = "NONE"

# === Simulating a Switch-Case Example ===
switch_case = {
    "development": {"db_url": "dev-db.example.com", "debug_mode": True, "log_level": "DEBUG"},
    "staging": {"db_url": "staging-db.example.com", "debug_mode": False, "log_level": "INFO"},
    "production": {"db_url": "prod-db.example.com", "debug_mode": False, "log_level": "ERROR"}
}

# Using the dictionary to simulate a switch-case
env_config = switch_case.get(env)

# Displaying the result
print(f"Environment: {env.capitalize()}")
print(f"Database URL: {env_config['db_url']}")
print(f"Debug Mode: {env_config['debug_mode']}")
print(f"Log Level: {env_config['log_level']}")
