var should = require('should')
var warmup = require('../warmup')
var Set = require('collections/set')
var exec = require('child_process').exec
var fs = require('fs')
var tempWriter = require('temp-write')


function anagram(s, t) {
  return s.split('').sort().join('') === t.split('').sort().join('')
}

function generatorToArray(generator, arg) {
  var result = []
  generator(arg, function (x) {result.push(x)})
  return result
}


describe('In the warmup module', function() {
  var change = warmup.change
  var stripQuotes = warmup.stripQuotes
  var scramble = warmup.scramble
  var powersOfTwo = warmup.powersOfTwo
  var prefixes = warmup.prefixes
  var interleave = warmup.interleave
  var stutter = warmup.stutter

  describe('change', function () {
    it('handles zero', function () {
      change(0).should.eql([0,0,0,0])
    })

    it('computes answers for small integer values fine', function () {
      change(97).should.eql([3, 2, 0, 2])
      change(8).should.eql([0, 0, 1, 3])
      change(250).should.eql([10, 0, 0, 0])
      change(144).should.eql([5, 1, 1, 4])
      change(97).should.eql([3, 2, 0, 2])
    })

    it('handles large values', function () {
      change(100000000000).should.eql([4000000000, 0, 0, 0])
    })
  })

  describe('stripQuotes', function () {
    it('works on the empty string', function () {
      stripQuotes('').should.eql('')
    })
    it('strips quotes properly for non-empty strings', function () {
      stripQuotes('Hello, world').should.eql('Hello, world')
      stripQuotes('\"\'').should.eql('')
      stripQuotes('a\"\"\'\"\"\"\"z').should.eql('az')
    })
  })

  describe('scramble', function () {
    it('scrambles properly', function () {
      ["a", "rat", "JavaScript testing", "", "zzz", "^*&^*&^▱ÄÈËɡɳɷ"].forEach(function (s) {
        anagram(s, scramble(s)).should.be.true
      })
    })
    it('is really random (produces all permutations)', function () {
      possibilities = new Set('ABC ACB BAC BCA CAB CBA'.split(' '))
      for (var i = 0; i < 200; i++) {
        possibilities.delete(scramble('ABC'))
      }
      possibilities.length.should.eql(0)
    })
  })

  describe('powersOfTwo', function () {
    it('generates sequences properly', function () {
      generatorToArray(powersOfTwo, -5).should.eql([])
      generatorToArray(powersOfTwo, 0).should.eql([])
      generatorToArray(powersOfTwo, 1).should.eql([1])
      generatorToArray(powersOfTwo, 63).should.eql([1, 2, 4, 8, 16, 32])
      generatorToArray(powersOfTwo, 64).should.eql([1, 2, 4, 8, 16, 32, 64])
    })
  })

  describe('prefixes', function () {
    it('generates sequences properly', function () {
      generatorToArray(prefixes, '').should.eql([''])
      generatorToArray(prefixes, 'a').should.eql(['', 'a'])
      generatorToArray(prefixes, 'ab').should.eql(['', 'a', 'ab'])
      generatorToArray(prefixes, 'abc').should.eql(['', 'a', 'ab', 'abc'])
    })
  })

  describe('interleave', function () {
    it('interleaves properly', function () {
      interleave([], []).should.eql([])
      interleave([1, 4, 6], []).should.eql([1, 4, 6])
      interleave([], [2, 3]).should.eql([2, 3])
      interleave([1], [9]).should.eql([1, 9])
      interleave([8, 8, 3, 9], [1]).should.eql([8, 1, 8, 3, 9])
      interleave([2], [7, '8', {}]).should.eql([2, 7, '8', {}])
    })
  })

  describe('stutter', function () {
    it('stutters properly', function () {
      stutter([], []).should.eql([])
      stutter([true]).should.eql([true, true])
      stutter([2, 'x']).should.eql([2, 2, 'x', 'x'])
      stutter([3, [4], 5]).should.eql([3, 3, [4], [4], 5, 5])
      stutter([1, [[[2]]], 3]).should.eql([1, 1, [[[2]]], [[[2]]], 3, 3])
    })
  })
})

describe('In the standalone scripts', function () {
  describe('fifa', function () {
    it('works for group G', function(done) {
      exec('node fifa2014group.js G', function (error, stdout, stderr) {
        lines = stdout.split(/\r?\n/)
        lines[0].should.match(/^Name\s*W\s*D\s*L/)
        lines[1].should.match(/^Germany\s*2\s*1\s*0/)
        lines[2].should.match(/^United States\s*1\s*1\s*1/)
        lines[3].should.match(/^Portugal\s*1\s*1\s*1/)
        lines[4].should.match(/^Ghana\s*0\s*1\s*2/)
        done()
      })
    })
    it('errors if no argument', function(done) {
      exec('node fifa2014group.js', function (error, stdout, stderr) {
        stderr.should.not.be.empty
        done()
      })
    })
    it('errors on argument Asdf', function(done) {
      exec('node fifa2014group.js Asdf', function (error, stdout, stderr) {
        stderr.should.not.be.empty
        done()
      })
    })
  })

  describe('lines', function () {
    it('works for a simple test case', function (done) {
      data = [
        '',
        '     ',
        '    one',
        'two',
        '    // comment',
        ' three   // comment',
        '// comment'
      ]
      file = tempWriter.sync(data.join('\n'))
      exec('node lines.js "' + file + '"' , function (error, stdout, stderr) {
        stdout.should.match(/^\s*3\s*$/)
        fs.unlink(file, function () {
          done()
        })
      })
    })
  })

  describe('wordcount', function () {
    it('works for a simple test case', function(done) {
      exec('echo "QQQ A abc\na  a\tHA:qQq" | node wordcount.js', function (error, stdout, stderr) {
        lines = stdout.split(/\r?\n/)
        lines[0].should.match(/^a 3\s*/)
        lines[1].should.match(/^abc 1\s*/)
        lines[2].should.match(/^ha 1\s*/)
        lines[3].should.match(/^qqq 2\s*/)
        done()
      })
    })
  })
})
