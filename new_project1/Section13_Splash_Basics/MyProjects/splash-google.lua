function main(splash, args)
  url = args.url
  assert(splash:go(url))
  assert(splash:wait(2))
  return {
    png = splash:png(),
    html = splash:html()
  }
end
