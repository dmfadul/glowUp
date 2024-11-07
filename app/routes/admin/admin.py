from flask import Blueprint, render_template

admin_bp = Blueprint('admin',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/admin/static')


@admin_bp.route('/report')
def index():
    return render_template('report.html')


@admin_bp.route('/view-logs')
def view_logs():
    return render_template('view-logs.html')