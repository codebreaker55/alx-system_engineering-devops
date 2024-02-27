#!/usr/bin/env ruby
# a Ruby script that matches capital letters
# The regular expression must be only matching: capital letters

puts ARGV[0].scan(/[A-Z]/).join
