function main(splash, args)
  url = args.url
  assert(splash:go(url))
  assert(splash:wait(2))
  
  input_box = assert(splash:select("#twotabsearchtextbox"))
  input_box:focus()
  input_box:send_text("books")
  assert(splash:wait(2))
  
  button = assert(splash:select("#nav-search-submit-button"))
  button:mouse_click()
  assert(splash:wait(5))
  return {
    html = splash:html(),
    png = splash:png(),
  }
end
