// Apple Vision text recognition, no install needed:  swift vision_ocr.swift screenshot.png
// Prints recognised lines so Claude reads ~300 tokens of text instead of a ~1,600-token image.
import Foundation
import Vision
import AppKit

let args = CommandLine.arguments
guard args.count > 1, let img = NSImage(contentsOfFile: args[1]),
      let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else {
    FileHandle.standardError.write("usage: swift vision_ocr.swift <image>\n".data(using: .utf8)!); exit(1)
}
let req = VNRecognizeTextRequest { r, _ in
    for o in (r.results as? [VNRecognizedTextObservation]) ?? [] {
        if let c = o.topCandidates(1).first { print(c.string) }
    }
}
req.recognitionLevel = .accurate
req.usesLanguageCorrection = true
try VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
