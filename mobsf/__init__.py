
def memory_limit():
    import resource
    """Limit max memory usage to half."""
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    
    # Convert KiB to bytes, and divide in two to half
    #po = int(get_memory() * 1024 / 2)
    resource.setrlimit(resource.RLIMIT_AS, (1503238553, hard))

memory_limit()
