include Jekyll

# this file is used to run the external python script to generate the search index
# we only want to run this script once, so we use the `:post_write` hook to run the script

Jekyll::Hooks.register :site, :post_write do |page|
  tag = 'Search index file path:'
  Jekyll.logger.info(tag, "Set search index file path")

  # set search file path
  if system "python3 scripts/set_search_file_path.py"
    Jekyll.logger.info(tag, "Search file path set")
  else
    Jekyll.logger.error(tag, "Failed to set searcg file path")
  end


end

