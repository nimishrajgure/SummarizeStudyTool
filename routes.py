from flask import Flask, request, jsonify, send_file, render_template, send_from_directory
from text_processing import text_summary, download_and_transcribe_youtube_video, segment_text
from fpdf_generation import generate_pdf

app = Flask(__name__)

# Define the index route
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Define the route to summarize video
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    youtube_url = data['youtube_url']
    output_path = "./yDownload"  # Change this to your desired output path

    transcribed_text = download_and_transcribe_youtube_video(youtube_url, output_path)

    if transcribed_text:
        # Segment the transcribed text
        segments = segment_text(transcribed_text)

        # Summarize each segment individually with bullet points
        summaries = []
        for i, segment in enumerate(segments, start=1):
            summary = text_summary(segment, maxlength=None)  # Adjust the maximum length as needed
            summary_with_bullet = f"{i}. {summary}"
            summaries.append(summary_with_bullet)

        # Combine individual summaries into a point-wise summary
        point_wise_summary = "\n".join(summaries)
        return jsonify({'success': True, 'summary_title': 'Summary', 'summary': point_wise_summary, 'transcribed_text': transcribed_text})
    else:
        return jsonify({'success': False, 'error': 'Failed to transcribe video'})

# Define the route to download PDF
@app.route('/download_pdf', methods=['POST'])
def download_pdf():
    data = request.get_json()
    summary_text = data['summary']

    pdf_output_path = "./summary.pdf"
    generate_pdf(summary_text, pdf_output_path)

    # Serve the generated PDF file for download
    return send_file(pdf_output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
