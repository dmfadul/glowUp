from flask import Blueprint, render_template
from app.models.user import User

admin_bp = Blueprint('admin',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/admin/static')


@admin_bp.route('/report')
def report():
    users_info = User.gen_report()

    print(users_info)

    return render_template('report.html', users_info=users_info)


@admin_bp.route('/view-logs')
def view_logs():
    return render_template('view-logs.html')