from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.models import User, Log

admin_bp = Blueprint('admin',
                    __name__,
                    template_folder='templates',
                    static_folder='static',
                    static_url_path='/admin/static')

@admin_bp.route('/adm')
def adm():
    return render_template('adm.html')


@admin_bp.route('/report')
@login_required
def report():
    # if not current_user.is_admin:
    #     return redirect(url_for('main.index'))
    
    users_info = User.gen_report()
    return render_template('report.html', users_info=users_info)


@admin_bp.route('/view-logs')
@login_required
def view_logs():
    # if not current_user.is_admin:
    #     return redirect(url_for('main.index'))
    
    logs = Log.get_report()
    return render_template('view-logs.html', logs=logs)